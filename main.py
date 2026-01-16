import logging
from analytics.loader import load_users
from analytics.metrics import active_users, average_age_by_country
from analytics.plots import plot_average_age


logging.basicConfig(level=logging.INFO)


def main():
    users = load_users("data/users.csv")

    active = active_users(users)
    logging.info(f"Active users count: {len(active)}")

    avg_age = average_age_by_country(active)
    plot_average_age(avg_age)


if __name__ == "__main__":
    main()
