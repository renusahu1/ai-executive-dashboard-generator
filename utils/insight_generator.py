def generate_insights(df, kpis):
    insights = []

    top_segment = (
        df[df["stage"] == "Won"]
        .groupby("customer_segment")["deal_value"]
        .sum()
        .sort_values(ascending=False)
    )

    if not top_segment.empty:
        insights.append(
            f"{top_segment.index[0]} is the strongest revenue segment, contributing the highest closed-won revenue."
        )

    if kpis["win_rate"] < 30:
        insights.append(
            "Win rate is below 30%, indicating a potential issue in lead qualification, proposal quality, or sales follow-up."
        )
    else:
        insights.append(
            "Win rate appears healthy, suggesting the current sales process is converting opportunities effectively."
        )

    if kpis["pipeline_value"] > kpis["total_revenue"]:
        insights.append(
            "Pipeline value is higher than closed revenue, showing future revenue potential but also requiring close monitoring of deal conversion."
        )

    avg_deal = kpis["avg_deal_size"]
    if avg_deal < 5000:
        insights.append(
            "Average deal size is relatively low, suggesting an opportunity to target larger accounts or improve upselling."
        )
    else:
        insights.append(
            "Average deal size is strong, indicating good potential for revenue scalability."
        )

    insights.append(
        "Recommended action: focus on high-performing customer segments, monitor aging pipeline deals, and improve conversion from proposal to closed-won."
    )

    return insights
