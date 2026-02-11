
from modules.hash_verifier import generate_hash
from modules.metadata_analyzer import get_metadata
from modules.case_manager import init_db, create_case
from modules.report_generator import generate_report

current_case = None
current_investigator = None

def menu():
    print("\n===== DEAK WER Forensic Toolkit =====")
    print("1. Create New Case")
    print("2. Analyze Evidence (Hash + Metadata + Report)")
    print("3. Exit")

init_db()

while True:
    menu()
    choice = input("Select option: ")

    if choice == "1":
        current_case = input("Enter Case Name: ")
        current_investigator = input("Investigator Name: ")
        create_case(current_case, current_investigator)
        print("Case Created Successfully!")

    elif choice == "2":
        if not current_case:
            print("Create a case first!")
            continue

        path = input("Enter evidence file path: ")

        hash_value = generate_hash(path)
        metadata = get_metadata(path)

        print("\nSHA256 Hash:", hash_value)
        print("Metadata:", metadata)

        report_file = generate_report(
            current_case,
            current_investigator,
            path,
            hash_value,
            metadata
        )

        print(f"\nReport Generated: {report_file}")

    elif choice == "3":
        print("Exiting DEAK WER...")
        break

    else:
        print("Invalid option")
