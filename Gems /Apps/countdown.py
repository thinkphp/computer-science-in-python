import time
import sys
import select
import os

def clear_screen():
    """
    Clears the terminal screen.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def countdown_timer(seconds):
    """
    Creates a countdown clock that displays the remaining time in a user-friendly format.

    Args:
        seconds (int): The total duration of the countdown in seconds.
    """
    while seconds > 0:
        minutes, secs = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        time_str = f"{hours:02d}:{minutes:02d}:{secs:02d}"
        print(time_str, end="\r")
        time.sleep(1)
        seconds -= 1

    # Final print to ensure countdown ends cleanly
    minutes, secs = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    time_str = f"{hours:02d}:{minutes:02d}:{secs:02d}"
    print(time_str)
    print("Countdown complete!")

def timer():
    """
    Creates a timer that starts when the user presses Enter and stops when they press Enter again.

    Displays the elapsed time in a user-friendly format.
    """
    print("Press Enter to start the timer.")
    input()  # Start timer
    start_time = time.time()
    print("Timer started. Press Enter to stop.")

    try:
        while True:
            elapsed_time = time.time() - start_time
            elapsed_time = int(elapsed_time)  # Convert to integer
            minutes, seconds = divmod(elapsed_time, 60)
            hours, minutes = divmod(minutes, 60)
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            print(time_str, end="\r")

            # Check if Enter has been pressed
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                input()  # Stop timer
                break
    except KeyboardInterrupt:
        pass

    print("\nTimer stopped.")

if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Countdown Clock")
        print("2. Timer")
        print("3. Exit")
        choice = input()

        if choice == "1":
            seconds = int(input("Enter the duration in seconds: "))
            countdown_timer(seconds)
        elif choice == "2":
            timer()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
