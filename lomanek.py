print("Tohle je testovací prográmek Lománek\n")
pokracovat = True
while pokracovat:  # Začátek cyklu
    otazka = float(input("Odpovíš nám na pár otázek ohledně Lománka? Víš třeba kolik je mu let? "))    # Tady se
    # ptáme na věk
    spravne = otazka == 37
    if spravne:
        print("Výborně. Jdeme dál")
    else:
        print("Řekl bych že to není dobře")
    otazka2 = input("Myslíš si, že je Lománek hodný? ")  # Otázka na vlastnosti
    varianta1 = (otazka2 == "ano" or otazka2 == "Ano" or otazka2 == "ANO")
    varianta2 = otazka2 == ""
    if varianta1:
        otazka21 = input("Jseš si jistý? ")  # Ujišťovací otázka zda opravdu ano
        spravne = (otazka21 == "ano" or otazka21 == "Ano" or otazka21 == "ANO")
        if spravne:
            print("Teda ty mu věříš!")
        else:
            print("Já si to myslel")
    elif varianta2:  # Když nezadám odpověď
        print("Když nevíš, tak nevíš")
    else:
        print("Někdy opravdu není")  # Varianta že není hodný
    otazka3 = input("A teď další. Zkus o Lománkovi napsat něco pěkného. ")  # Zkouška s délkou výrazu
    staci = len(otazka3) >= 10
    if staci:
        print("Vypádá to, že ho opravdu znáš")
    else:
        print("To je vše? Nic moc teda")
    print("Na závěr tady mám jeden vzkaz pro Lománka. Klikni a uvidíš jej.")    # Vzkaz pro Romču
    input()
    from turtle import left, right, forward, exitonclick
    left(45)
    forward(50)
    left(45)
    forward(30)
    left(45)
    forward(10)
    left(45)
    forward(20)
    left(45)
    forward(10)
    right(45)
    forward(10)
    right(45)  # Druhá půlka srdce
    forward(10)
    left(45)
    forward(20)
    left(45)
    forward(10)
    left(45)
    forward(30)
    left(45)
    forward(50)
    left(45)
    forward(10)
    exitonclick()

    spustit_znovu = input("Chceš to zkusit znovu? Y/N ")  # Opakování
    ano = (spustit_znovu == "Y" or spustit_znovu == "y")
    if ano:
        continue
    else:
        break
print("\nDíky za účast")
input("Stisknutím klávesy zavřeš tohle okno")
