import json

def update_user_data(file_path, user_id, updated_data):
    """
    Updates the user data in the JSON file.

    :param file_path: Path to the JSON file containing user data.
    :param user_id: ID of the user to update.
    :param updated_data: Dictionary containing updated user data.
    """
    try:
        # Load existing data from the file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Check if user exists
        if user_id in data:
            # Update user data
            data[user_id].update(updated_data)
            print(f"User {user_id} data updated successfully.")
        else:
            print(f"User {user_id} not found. Adding new user.")
            data[user_id] = updated_data

        # Save updated data back to the file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    except FileNotFoundError:
        print(f"File not found. Creating a new file and adding user {user_id}.")
        data = {user_id: updated_data}
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    except json.JSONDecodeError:
        print("Error decoding JSON. Please check the file format.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    file_path = "user_data.json"
    user_id = "12345"
    updated_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 30
    }

    update_user_data(file_path, user_id, updated_data)