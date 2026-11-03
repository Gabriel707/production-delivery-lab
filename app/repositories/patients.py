from app.db.db import get_connection


def list_patients():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, name, status, created_at
                FROM patients
                ORDER BY id;
                """
            )

            patients = cur.fetchall()

    return [
        {
            "id": patient[0],
            "name": patient[1],
            "status": patient[2],
            "created_at": patient[3],
        }
        for patient in patients
    ]


def create_patient(name: str, status: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO patients (name, status)
                VALUES (%s, %s)
                RETURNING id, name, status, created_at;
                """,
                (name, status),
            )

            patient = cur.fetchone()

    return {
        "id": patient[0],
        "name": patient[1],
        "status": patient[2],
        "created_at": patient[3],
    }