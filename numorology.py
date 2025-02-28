# Function to reduce a number to a single digit or master number (11, 22, 33)
def reduce_number(n):
    while n >= 10 and n not in [11, 22, 33]:  # Master numbers are not reduced
        n = sum(map(int, str(n)))
    return n


# Function to calculate Life Path Number
def calculate_life_path_number(date_of_birth):
    day, month, year = map(int, date_of_birth.split('/'))
    day = reduce_number(day)
    month = reduce_number(month)
    year = reduce_number(year)
    life_path_number = reduce_number(day + month + year)
    return life_path_number


# Function to calculate Destiny Number
def calculate_destiny_number(full_name):
    # Numerology chart: A=1, B=2, ..., Z=26
    name_to_number = {chr(64 + i): i for i in range(1, 27)}
    total = 0
    for char in full_name.upper():
        if char in name_to_number:
            total += name_to_number[char]
    return reduce_number(total)


# Function to calculate Soul Urge Number
def calculate_soul_urge_number(full_name):
    # Only vowels are considered
    vowels = {'A', 'E', 'I', 'O', 'U'}
    name_to_number = {chr(64 + i): i for i in range(1, 27)}
    total = 0
    for char in full_name.upper():
        if char in vowels and char in name_to_number:
            total += name_to_number[char]
    return reduce_number(total)


# Function to calculate Personality Number
def calculate_personality_number(full_name):
    # Only consonants are considered
    vowels = {'A', 'E', 'I', 'O', 'U'}
    name_to_number = {chr(64 + i): i for i in range(1, 27)}
    total = 0
    for char in full_name.upper():
        if char not in vowels and char in name_to_number:
            total += name_to_number[char]
    return reduce_number(total)


# Main function
def main():
    # Input date of birth and full name
    date_of_birth = input("Enter your date of birth (DD/MM/YYYY): ")
    full_name = input("Enter your full name: ")

    # Calculate numerology numbers
    life_path_number = calculate_life_path_number(date_of_birth)
    destiny_number = calculate_destiny_number(full_name)
    soul_urge_number = calculate_soul_urge_number(full_name)
    personality_number = calculate_personality_number(full_name)

    # Display results
    print("\n--- Numerology Report ---")
    print(f"Life Path Number: {life_path_number}")
    print(f"Destiny Number: {destiny_number}")
    print(f"Soul Urge Number: {soul_urge_number}")
    print(f"Personality Number: {personality_number}")

    # Interpretations
    interpretations = {
        "Life Path Number": {
            1: "The Leader - Independent, ambitious, and innovative.",
            2: "The Peacemaker - Cooperative, diplomatic, and intuitive.",
            3: "The Communicator - Creative, expressive, and social.",
            4: "The Builder - Practical, disciplined, and hardworking.",
            5: "The Adventurer - Freedom-loving, adaptable, and curious.",
            6: "The Nurturer - Responsible, caring, and compassionate.",
            7: "The Seeker - Analytical, introspective, and spiritual.",
            8: "The Achiever - Ambitious, authoritative, and success-oriented.",
            9: "The Humanitarian - Compassionate, idealistic, and selfless.",
            11: "The Visionary - Intuitive, inspirational, and spiritually aware.",
            22: "The Master Builder - Practical, visionary, and transformative.",
            33: "The Master Teacher - Compassionate, uplifting, and spiritually evolved."
        },
        "Destiny Number": {
            1: "You are destined to lead and inspire others.",
            2: "You are destined to bring harmony and balance.",
            3: "You are destined to express creativity and joy.",
            4: "You are destined to build a solid foundation for the future.",
            5: "You are destined to embrace change and adventure.",
            6: "You are destined to nurture and care for others.",
            7: "You are destined to seek knowledge and wisdom.",
            8: "You are destined to achieve material success and power.",
            9: "You are destined to serve humanity and make a difference.",
            11: "You are destined to inspire and enlighten others.",
            22: "You are destined to turn dreams into reality.",
            33: "You are destined to teach and heal on a global scale."
        },
        "Soul Urge Number": {
            1: "You desire independence and self-expression.",
            2: "You desire love, harmony, and partnership.",
            3: "You desire creativity, joy, and self-expression.",
            4: "You desire stability, security, and order.",
            5: "You desire freedom, adventure, and variety.",
            6: "You desire love, family, and responsibility.",
            7: "You desire knowledge, introspection, and spirituality.",
            8: "You desire success, power, and achievement.",
            9: "You desire compassion, service, and humanitarianism.",
            11: "You desire spiritual enlightenment and inspiration.",
            22: "You desire to manifest your dreams into reality.",
            33: "You desire to teach, heal, and uplift humanity."
        },
        "Personality Number": {
            1: "Others see you as a leader and innovator.",
            2: "Others see you as a peacemaker and diplomat.",
            3: "Others see you as creative and expressive.",
            4: "Others see you as practical and disciplined.",
            5: "Others see you as adventurous and adaptable.",
            6: "Others see you as nurturing and responsible.",
            7: "Others see you as analytical and introspective.",
            8: "Others see you as ambitious and authoritative.",
            9: "Others see you as compassionate and idealistic.",
            11: "Others see you as intuitive and inspirational.",
            22: "Others see you as visionary and transformative.",
            33: "Others see you as wise and spiritually evolved."
        }
    }

    # Display interpretations
    print("\n--- Interpretations ---")
    for key, value in interpretations.items():
        if key == "Life Path Number":
            number = life_path_number
        elif key == "Destiny Number":
            number = destiny_number
        elif key == "Soul Urge Number":
            number = soul_urge_number
        elif key == "Personality Number":
            number = personality_number
        if number in value:
            print(f"{key}: {value[number]}")
        else:
            print(f"{key}: Your number is unique and special!")


# Run the program
if __name__ == "__main__":
    main()
