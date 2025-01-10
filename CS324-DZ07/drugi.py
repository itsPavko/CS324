import sqlite3


def kreiraj_bazu():
    
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
   
    cursor.execute('''
    CREATE TABLE predmeti (
        sifra TEXT,
        punoIme TEXT,
        profesor TEXT,
        godinaStudiranja INTEGER
    )
    ''')
    
  
    predmeti = [
        ("IT101", "Python", "Dr. Andrea Busic", 1),
        ("MA102", "Matematika I", "Prof. Djurdja Tomic", 1),
        ("IT350", "Matematika II", "Dr. Petra Gusic", 1),
        ("CS201", "Baze podataka", "Prof. Tara Zattila", 2),
        ("MA202", "Verovatnoca II", "Prof. Mila Marinkov", 2),
        ("CS301", "Algoritmi i strukture podataka", "Milica Stefanovic", 3),
        ("CS103", "Skripting", "Prof. Jovana Petrovic", 3)
    ]
    
    
    cursor.executemany('''
    INSERT INTO predmeti (sifra, punoIme, profesor, godinaStudiranja)
    VALUES (?, ?, ?, ?)
    ''', predmeti)
    
  
    conn.commit()
    
    return conn, cursor

def pretrazi_po_profesoru(conn, profesor):
    cursor = conn.cursor()
    
   
    cursor.execute('''
    SELECT sifra, punoIme, godinaStudiranja FROM predmeti
    WHERE profesor = ?
    ''', (profesor,))
    
    rezultati = cursor.fetchall()
    
    return rezultati


if __name__ == "__main__":
   
    conn, cursor = kreiraj_bazu()
    
    
    profesor = "Prof. Djurdja Tomic"
    rezultati = pretrazi_po_profesoru(conn, profesor)
    
    print(f"Predmeti koje predaje {profesor}:")
    for predmet in rezultati:
        sifra, punoIme, godinaStudiranja = predmet
        print(f"{sifra} - {punoIme}, Godina: {godinaStudiranja}")
    
   
    conn.close()
