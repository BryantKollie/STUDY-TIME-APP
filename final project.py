import time

def play_alarm():
    print('\a')
    time.sleep(1)
    print('\a')
    time.sleep(1)
    print('\a')

def main():
    print("🧠 Welcome to the Study Timer App! 🧠")
    study_minutes = int(input("Enter study time in minutes: "))
    print(f"\n📚 Study session for {study_minutes} minutes has started! Stay focused... 📚")
    time.sleep(study_minutes * 60)  # Wait quietly for study time
    
    print("\n🎉 Study time is over! Time for a break! 🎉")
    play_alarm()

    print("\n🛌 10-minute break has started. Relax! 🛌")
    time.sleep(10 * 60)  # Wait quietly for break time
    
    print("\n✅ Break time is over! Good job completing your session! ✅")
    play_alarm()

if __name__ == "__main__":
    main()
