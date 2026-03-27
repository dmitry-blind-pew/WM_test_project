ONE_ROW_EXPECTED = [
    {
        "student": "Алексей Смирнов",
        "date": "2024-06-01",
        "coffee_spent": "450",
        "sleep_hours": "4.5",
        "study_hours": "12",
        "mood": "норм",
        "exam": "Математика",
    }
]

STANDARD_EXPECTED = [
    {
        "student": "Алексей Смирнов",
        "date": "2024-06-01",
        "coffee_spent": "400",
        "sleep_hours": "4.5",
        "study_hours": "12",
        "mood": "норм",
        "exam": "Математика",
    },
    {
        "student": "Алексей Смирнов",
        "date": "2024-06-02",
        "coffee_spent": "500",
        "sleep_hours": "4.0",
        "study_hours": "14",
        "mood": "устал",
        "exam": "Математика",
    },
    {
        "student": "Дарья Петрова",
        "date": "2024-06-01",
        "coffee_spent": "200",
        "sleep_hours": "7.0",
        "study_hours": "6",
        "mood": "отл",
        "exam": "Математика",
    },
]

TWO_FILES_EXPECTED = ONE_ROW_EXPECTED + STANDARD_EXPECTED

EMPTY_EXPECTED = []

ONE_ROW_MEDIAN_EXPECTED = [["Алексей Смирнов", 450.0]]
STANDARD_MEDIAN_EXPECTED = [["Алексей Смирнов", 450.0], ["Дарья Петрова", 200.0]]
