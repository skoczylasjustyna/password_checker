
#Sprawdzarka haseł - dobre hasło powinno mieć minimum 8 znaków oraz zawierać małe i duże litery

password = input("Podaj nowe hasło: ")

has_lower = False
has_upper = False

#sprawdzenie czy długość hasła spełnia wymagania - dobre hasło ma mieć 8 lub więcej znaków
prop_len = len(password) >= 8
#ile znaków brakuje do ich odpowiedniej minimalnej liczby?
len_lack = 8 - len(password)

for char in password:  # znak po znaku sprawdzaj, czy hasło zawiera litery i liczby oraz małe i duże litery
    if char.isalnum() and char.isupper():
        has_upper = True
    if char.isalnum() and char.islower():
        has_lower = True

#hasło jest odpowiednie jeśli spełnia powyższe warunki
is_correct = has_lower and has_upper and prop_len
if is_correct:
    print("Twoje hasło jest wystarczająco złożone")
else:
    print("Twoje hasło jest zbyt słabe, zmodyfikuj je:")
    if not has_lower:
        print("- dodaj przynajmniej jedną małą literę")
    if not has_upper:
        print("- dodaj przynajmniej jedną dużą literę")
    if not prop_len:
      print(f"- hasłu brakuje jeszcze {len_lack} lub więcej znaków ")