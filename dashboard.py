import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set the style for seaborn
sns.set(style='darkgrid')

# Simulated data for demonstration
monthly_orders_data = {
    'month': ['January', 'February', 'March', 'April', 'May'],
    'total_orders': [120, 150, 200, 180, 160]
}
monthly_orders_df = pd.DataFrame(monthly_orders_data)

bystate_data = {
    'customer_state': ['CA', 'TX', 'NY', 'FL', 'IL'],
    'customer_count': [50, 40, 30, 20, 10]
}
bystate_df = pd.DataFrame(bystate_data)

# Streamlit app layout
st.set_page_config(page_title="Olist Store Dashboard", layout="wide")  # Wider layout
st.title('Olist Store Dashboard :sparkles:')
st.markdown("Welcome to the Olist Store data dashboard! Here, you can explore the monthly orders and customer distribution by state.")

# Sidebar for additional information
st.sidebar.header("Dashboard Controls")
st.sidebar.info("Navigate the marketplace landscape! Use this dashboard to uncover powerful insights and optimize your business strategies.")
st.sidebar.image("dashboard/logo.png", width=200)  # Company logo

# Monthly Orders Plot
st.subheader("📅 Number of Orders per Month")
plt.figure(figsize=(10, 5))
plt.plot(monthly_orders_df["month"], monthly_orders_df["total_orders"], marker='o', linewidth=2, color="#72BCD4", label="Total Orders")
plt.title("Monthly Orders", loc="center", fontsize=20)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True)
plt.legend()
st.pyplot(plt)  # Display the plot in the Streamlit app

# Customer by State Plot
st.subheader("🌍 Number of Customers by State")
plt.figure(figsize=(10, 5))
colors_ = sns.color_palette("Blues", len(bystate_df))  # Use a color palette
sns.barplot(
    x="customer_count",
    y="customer_state",
    data=bystate_df.sort_values(by="customer_count", ascending=False),
    palette=colors_,
    hue=None,
    legend=False  
)
plt.title("Customer Distribution by State", loc="center", fontsize=20)
plt.ylabel("States", fontsize=12)
plt.xlabel("Customer Count", fontsize=12)
plt.tick_params(axis='y', labelsize=12)
st.pyplot(plt)  # Display the plot in the Streamlit app

# Footer
st.markdown("---")
st.markdown("### Contact Information")
st.markdown("If you have any questions, please contact us at support@olist.com.")
