def calculate_kpis(df):
    total_revenue = df[df["stage"] == "Won"]["deal_value"].sum()
    avg_deal_size = df["deal_value"].mean()

    total_closed = df[df["stage"].isin(["Won", "Lost"])]
    won_deals = df[df["stage"] == "Won"]

    win_rate = (len(won_deals) / len(total_closed) * 100) if len(total_closed) > 0 else 0

    pipeline_value = df[df["stage"].isin(["Proposal", "Negotiation", "Qualified"])]["deal_value"].sum()

    return {
        "total_revenue": total_revenue,
        "avg_deal_size": avg_deal_size,
        "win_rate": win_rate,
        "pipeline_value": pipeline_value
    }
