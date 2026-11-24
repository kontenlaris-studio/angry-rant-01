import os

RANT = (
    "My printer only runs out of ink at 8:59 a.m., one minute before the meeting. "
    "It sat there all weekend, fully loaded, perfectly happy, waiting. I fed it "
    "paper, I fed it love, I installed three different drivers, and it still "
    "blinks at me like I am the problem. I am buying a typewriter. A typewriter "
    "has never once asked me to update its firmware before it will print one page."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT + "\n")


if __name__ == "__main__":
    main()
