from protocols.bio_adaptation import HumanSystem

def run_example():
    my_os = HumanSystem()
    # 昨日のような「調和した食事」の例
    daily_event = {
        "event_name": "International Dinner",
        "artificial_additives": False,
        "is_local_season": True
    }
    score = my_os.evaluate_input(daily_event)
    print(f"Harmony Score: {score}")

if __name__ == "__main__":
    run_example()
