from tabulate import tabulate

from Bloom.check_password_uniqueness import check_password_uniqueness
from Bloom.BloomFilter import BloomFilter
from Hyper.set_productivity import set_productivity
from Hyper.hyperloglog_productivity import hyperloglog_productivity
from helper.data_loader import data_loader


def main():
    backspaces = "_"*20
    print(f"\n{backspaces}TASK 1{backspaces}\n")

    bloom = BloomFilter(size=1000, num_hashes=3)

    existing_passwords = ["password123", "admin123", "qwerty123"]
    for password in existing_passwords:
        bloom.add(password)

    new_passwords_to_check = ["password123",
                              "newpassword", "admin123", "guest"]
    results = check_password_uniqueness(bloom, new_passwords_to_check)

    for password, status in results.items():
        print(f"Пароль '{password}' - {status}.")

    print(f"\n{backspaces}TASK 2{backspaces}\n")

    file_path = "/src/data/lms-stage-access.log"
    try:
        ips = data_loader(file_path)

        set = set_productivity(ips)
        hyper = hyperloglog_productivity(ips)
    except Exception as e:
        print(f"An error occurred: {e}")

    print(tabulate([["Унікальні елементи", set["unique"], hyper["unique"]], [
          "Час виконання", set["time"], hyper["time"]]], headers=["   ", "Точний підрахунок", "HyperLog"]))


if __name__ == "__main__":
    main()
