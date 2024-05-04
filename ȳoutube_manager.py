import json


def load_data():
    try:
        with open('youtube.txt','r') as file:
            test = json.load(file)
    except FileExistsError:
        return []
 
 
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f'{index}. {video['name']},Duration: {video['time']}')

def add_videos(videos):
    name = input("Enter videos name: ")
    time = input("Enter video time: ")
    
    videos.append({'name':name, 'time':time})


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the videos number to be updated"))
    if 1 <=index<=len(videos):
        name = input("Enter video name: ")
        time = input("Enter video time: ")
        
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid Index selection")
        
        
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the videos number to be deleted"))
    if 1 <= index <=len(videos):
        del videos(index-1)
        save_data_helper(videos)
        print("Your video is deleted")
    else:
         print("Invalid Index selection")
        
def main():
    videos = load_data()

    while True:
        print("\n Youyube manager | Choose an option")
        print("1. List all your Youtube videos")
        print('2. Add a youtube videos')
        print("3. Update a youtube details")
        print('4. Dleted a youtube videos')
        
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case '3':
                update_video(videos)
            case 4:
                delete_video(videos)        
            case _:
                print("Inavlid Choice")

if __name__=="__main__":
    main()
        