from datetime import datetime
import json
from json.decoder import JSONDecodeError
import uuid

class Task:

    def __init__(self,id : str, desc : str, status : str, created_at : datetime, updated_at :datetime) -> None:
        self.id = id
        self.desc = desc
        self.status = status # todo, in-progress, done
        self.created_at = created_at
        self.updated_at = updated_at


    @staticmethod
    def add_task() -> None:
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError, JSONDecodeError):
            data = {"tasks": []}

        desc = input("\nEnter a description for the new task: ")
        id = str(uuid.uuid4())
        status = "N/A"
        created_at = datetime.now().isoformat()
        updated_at = datetime.now().isoformat()

        
        while True:
            print("\n Select the status of the new task")
            print("1. todo")
            print("2. in-progress")
            print("3. done")

            choice = input(">> ").strip()

            if choice == "1":
                status = "todo"
                break
            elif choice == "2":
                status = "in-progress"
                break
            elif choice == "3":
                status = "done"
                break
            else :
                print("Invalid input, try again.")


        new_task = {
            "id": id,
            "status":status,
            "created_at":created_at,
            "updated_at":updated_at,
            "description": desc
        }

        data["tasks"].append(new_task)

        with open("tasks.json", "w") as f:
            json.dump(data, f, indent = 4)

        print(f"\n The new task with id: {id} was added.")

        