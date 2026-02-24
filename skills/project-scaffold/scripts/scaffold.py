import argparse
import os
import shutil
from pathlib import Path

# Paths to the reference folder structures stored in the skill's references directory
REFERENCES_DIR = Path(__file__).parent.parent / "references"

STRUCTURES = {
    "data_analysis": "data_analysis_structure.md",
    "ml_dl": "ml_dl_structure.md",
    "stat_modeling": "stat_modeling_structure.md",
    "agent": "agent_structure.md"
}

def create_scaffold(project_name: str, task_type: str, output_dir: str):
    """
    Creates the directory structure for the specified task type.
    """
    if task_type not in STRUCTURES:
        print(f"Error: Unknown task type '{task_type}'.")
        print(f"Available types: {', '.join(STRUCTURES.keys())}")
        return

    base_path = Path(output_dir) / project_name
    print(f"🚀 Creating {task_type} project scaffold at: {base_path}")

    # Define the directories to create based on the task type
    # We only create directories, NOT the mock files as requested.
    directories = []
    
    if task_type == "data_analysis":
        directories = [
            "config",
            "data/raw",
            "data/interim",
            "data/processed",
            "notebooks",
            "src/analysis",
            "src/utils",
            "src/visualization",
            "output/models",
            "output/figures",
            "output/reports",
            "tests"
        ]
    elif task_type == "ml_dl":
        directories = [
            "data",
            "experiments",
            "notebooks",
            "papers",
            "src/models",
            "configs/model",
            "configs/dataset",
            "configs/experiment"
        ]
    elif task_type == "stat_modeling":
        directories = [
            "data/raw",
            "data/processed",
            "notebooks",
            "src",
            "reports"
        ]
    elif task_type == "agent":
        directories = [
            "agents",
            "tools",
            "memory",
            "config",
            "tests"
        ]

    # Create the directories
    base_path.mkdir(parents=True, exist_ok=True)
    for dir_path in directories:
        (base_path / dir_path).mkdir(parents=True, exist_ok=True)
        # Add a .gitkeep file to ensure empty directories are tracked by git
        with open(base_path / dir_path / ".gitkeep", "w") as f:
            pass

    # Always create a README.md file
    readme_path = base_path / "README.md"
    if not readme_path.exists():
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write("")

    print(f"✅ Successfully created directory structure for {task_type}")
    
    # Also tell the user to check the reference file for the full recommended structure
    ref_file = STRUCTURES[task_type]
    print(f"\n💡 Note: Only the folder structure was created. For the complete recommended setup including example files, please refer to:")
    print(f"   {REFERENCES_DIR / ref_file}")

def main():
    parser = argparse.ArgumentParser(description="Create project scaffolds based on task type.")
    parser.add_argument("project_name", help="Name of the project directory to create")
    parser.add_argument("--task", required=True, choices=list(STRUCTURES.keys()), 
                        help="The type of task for the project scaffold")
    parser.add_argument("--path", default=".", help="Output directory path (default: current directory)")
    
    args = parser.parse_args()
    
    create_scaffold(args.project_name, args.task, args.path)

if __name__ == "__main__":
    main()
