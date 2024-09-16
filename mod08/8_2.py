import mysql.connector

def hae_lentokentat_tyypeittain(maakoodi, yhteys):
    sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type"


    try:
        kursori = yhteys.cursor()
        kursori.execute(sql, (maakoodi,))
        tulokset = kursori.fetchall()


        if tulokset:
            print(f"Lentokenttien lukumäärät tyypeittäin maassa {maakoodi}:")
            for tyyppi, maara in tulokset:
                print(f"{tyyppi.capitalize()}: {maara} kappaletta")

    finally:
        kursori.close()


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='jimias',
    password='dobronx',
    autocommit=True
)


if __name__ == "__main__":
    maakoodi = input("Anna maakoodi (esimerkiksi FI): ").upper()
    hae_lentokentat_tyypeittain(maakoodi, yhteys)
    yhteys.close()