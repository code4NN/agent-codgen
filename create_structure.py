import os
import yaml

def create_from_manifest(manifest_path: str):
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    root = manifest.get("project_root", ".")
    print(f"📁 Creating project structure at: {os.path.abspath(root)}")

    def write_file(path: str, content: str | None):
        if os.path.exists(path):
            return  # NEVER overwrite
        with open(path, "w", encoding="utf-8") as f:
            f.write(content or "")

    def create_dirs(base_path: str, directories: dict):
        for dir_name, spec in directories.items():
            dir_path = os.path.join(base_path, dir_name)
            os.makedirs(dir_path, exist_ok=True)

            files = spec.get("files", {})
            for file_name, file_spec in files.items():
                file_path = os.path.join(dir_path, file_name)
                content = file_spec.get("content") if isinstance(file_spec, dict) else ""
                write_file(file_path, content)

            subdirs = spec.get("directories", {})
            create_dirs(dir_path, subdirs)

    create_dirs(root, manifest.get("directories", {}))

    for file_name, file_spec in manifest.get("files", {}).items():
        file_path = os.path.join(root, file_name)
        content = file_spec.get("content") if isinstance(file_spec, dict) else ""
        write_file(file_path, content)

    print("✅ Directory structure and files created successfully")

if __name__ == "__main__":
    create_from_manifest("structure.yaml")
