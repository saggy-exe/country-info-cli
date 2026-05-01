def format_country(country):
    name = country["name"]["common"]
    flag = country.get("flag", "")

    capital = ", ".join(country.get("capital", ["N/A"]))
    population = f"{country.get('population', 0):,}"
    region = country.get("region", "N/A")

    languages = ", ".join(country.get("languages", {}).values()) or "N/A"

    currencies = ", ".join(
        f"{v['name']} ({k})"
        for k, v in country.get("currencies", {}).items()
    ) or "N/A"

    print("\n" + "=" * 50)
    print(f"{name} {flag}")
    print("=" * 50)
    print(f"{'Capital':<15}: {capital}")
    print(f"{'Population':<15}: {population}")
    print(f"{'Region':<15}: {region}")
    print(f"{'Languages':<15}: {languages}")
    print(f"{'Currencies':<15}: {currencies}")
    print("=" * 50 + "\n")


def format_history(rows):
    print("\n" + "=" * 70)
    print(f"{'Country':<15}{'Capital':<20}{'Region':<15}{'Time'}")
    print("=" * 70)

    for name, capital, pop, region, time in rows:
        print(f"{name:<15}{capital:<20}{region:<15}{time}")

    print("=" * 70 + "\n")


def compare_countries(c1, c2):
    def fmt(val1, val2):
        return f"{val1} | {val2}" if val1 == val2 else f"{val1} ≠ {val2}"

    print("\n" + "=" * 60)
    print(f"{c1['name']['common']} vs {c2['name']['common']}")
    print("=" * 60)

    print(f"{'Capital':<15}: {fmt(c1['capital'][0], c2['capital'][0])}")
    print(f"{'Region':<15}: {fmt(c1['region'], c2['region'])}")
    print(f"{'Population':<15}: {fmt(c1['population'], c2['population'])}")

    print("=" * 60 + "\n")


def format_stats(stat):
    if stat:
        region, count = stat
        print(f"\nMost searched region: {region} ({count} searches)\n")
    else:
        print("\nNo data yet.\n")