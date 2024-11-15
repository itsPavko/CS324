from getpass import getpass

def proveri_korisnika():
    ispravno_korisnicko_ime = "korisnik"
    ispravna_lozinka = "lozinka123"

    uneto_korisnicko_ime = input("Unesite korisničko ime: ")

    if uneto_korisnicko_ime != ispravno_korisnicko_ime:
        print("Pogrešno korisničko ime.")
        return

    uneta_lozinka = getpass("Unesite lozinku: ")

    if uneta_lozinka != ispravna_lozinka:
        print("Pogrešna lozinka.")
        return

    print("Uspešno ste se ulogovali!")

proveri_korisnika()