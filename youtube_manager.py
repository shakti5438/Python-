import json

def load_data():
    try: 
        with open('youtube.text', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.text', 'w') as file:
        json.dump(videos, file)

def list_all_video(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")

    input("Enter to back")


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")

    videos.append({'name': name, 'time': time})
    save_data_helper(videos)


def update_video(videos):
    list_all_video(videos)
    index = int(input("Enter the video number to be updated"))
    if 1 <= index <= len(videos):
        name = input("Enter video name: ")
        time = input("Enter video time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid Index Selection")


def delete_video(videos):
    list_all_video(videos)
    index = int(input("Enter the video number to be deleted"))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("your video is deleted ")
    else:
        print("Invalid Index Selection ")


def main():
    videos = load_data()

    while True:
        print("\n Youtube manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)

            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()