papers = int(input())
reading_papers_for_one_hour = int(input())
days = int(input())

hours_for_reading_the_book = papers / reading_papers_for_one_hour
needed_hours_per_day = hours_for_reading_the_book / days

print(int(needed_hours_per_day))