import csv
import json

data = {
    'summary': {},
    'categories': [],
    'transactions': []
}

month_numbers = {
    'January': '01', 'February': '02', 'March': '03', 'April': '04',
    'May': '05', 'June': '06', 'July': '07', 'August': '08',
    'September': '09', 'October': '10', 'November': '11', 'December': '12'
}

# 1. Agency Salary (June 2026 - October 2026)
with open('freelance_agency_salary.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        mnum = month_numbers.get(r['Month'], '06')
        data['transactions'].append({
            'source': 'Agency Salary',
            'category_id': 'agency',
            'date': f"{r['Month']} {r['Year']}",
            'iso_date': f"{r['Year']}-{mnum}-01",
            'time': '12:00 PM',
            'month': r['Month'],
            'year': int(r['Year']),
            'amount': float(r['Amount_INR']),
            'type': 'Credit',
            'status': 'Completed',
            'details': r['Description']
        })

# 2. College Freelance
with open('freelance_college_work.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        data['transactions'].append({
            'source': 'College Freelance',
            'category_id': 'college',
            'date': r['Date'],
            'iso_date': r['Date'],
            'time': r['Time'],
            'month': r['Month'],
            'year': int(r['Year']),
            'amount': float(r['Amount']),
            'type': 'Credit',
            'status': 'Completed',
            'details': 'Student Freelance Project Payout'
        })

# 3. Digital Products
with open('digital_product_sale_revenue.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        mnum = month_numbers.get(r['Month'], '01')
        day = r['Date'].split('-')[0].zfill(2)
        data['transactions'].append({
            'source': 'Digital Products',
            'category_id': 'digital',
            'date': r['Date'],
            'iso_date': f"{r['Year']}-{mnum}-{day}",
            'time': r['Time'],
            'month': r['Month'],
            'year': int(r['Year']),
            'amount': float(r['Amount_INR']),
            'type': 'Credit',
            'status': r['Status'],
            'details': f"{r['Transactions_Count']} sale(s) completed"
        })

# 4. Razorpay
with open('razorpay_earnings.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        mnum = month_numbers.get(r['Month'], '04')
        day = r['Date'].split('-')[0].zfill(2)
        data['transactions'].append({
            'source': 'Razorpay',
            'category_id': 'razorpay',
            'date': r['Date'],
            'iso_date': f"{r['Year']}-{mnum}-{day}",
            'time': r['Time'],
            'month': r['Month'],
            'year': int(r['Year']),
            'amount': float(r['Amount_INR']),
            'type': 'Credit',
            'status': 'Completed',
            'details': 'Razorpay Payment Gateway Capture'
        })

# 5. Review Work
data['transactions'].append({
    'source': 'Review Work',
    'category_id': 'review',
    'date': 'June 2025',
    'iso_date': '2025-06-15',
    'time': '10:00 AM',
    'month': 'June',
    'year': 2025,
    'amount': 90.00,
    'type': 'Credit',
    'status': 'Completed',
    'details': 'Initial Product Review Bounty'
})

total_earned = sum(t['amount'] for t in data['transactions'])

category_meta = [
    {
        'id': 'agency',
        'name': 'Agency Salary',
        'color': '#dcf836',
        'icon': 'briefcase'
    },
    {
        'id': 'college',
        'name': 'College Freelance',
        'color': '#b4f044',
        'icon': 'graduation'
    },
    {
        'id': 'digital',
        'name': 'Digital Products',
        'color': '#f2f059',
        'icon': 'shopping-bag'
    },
    {
        'id': 'razorpay',
        'name': 'Razorpay Payments',
        'color': '#8ef57e',
        'icon': 'credit-card'
    },
    {
        'id': 'review',
        'name': 'Review Work',
        'color': '#d7f283',
        'icon': 'star'
    }
]

for meta in category_meta:
    cat_txs = [t for t in data['transactions'] if t['category_id'] == meta['id']]
    cat_sum = sum(t['amount'] for t in cat_txs)
    cat_count = len(cat_txs)
    cat_share = round((cat_sum / total_earned) * 100, 2) if total_earned > 0 else 0
    data['categories'].append({
        'id': meta['id'],
        'name': meta['name'],
        'color': meta['color'],
        'amount': round(cat_sum, 2),
        'tx_count': cat_count,
        'share': cat_share,
        'icon': meta['icon']
    })

timeline_order = [
    ('June', 2025),
    ('January', 2026), ('February', 2026), ('March', 2026), ('April', 2026), ('May', 2026),
    ('June', 2026), ('July', 2026), ('August', 2026), ('September', 2026), ('October', 2026)
]

monthly_data = []
running_cumulative = 0.0

for m, y in timeline_order:
    txs = [t for t in data['transactions'] if t['month'] == m and t['year'] == y]
    earned = sum(t['amount'] for t in txs if t['type'] == 'Credit')
    running_cumulative += earned
    monthly_data.append({
        'month': m,
        'year': y,
        'label': f"{m} {y}",
        'short_label': f"{m[:3]} '{str(y)[2:]}",
        'earned': round(earned, 2),
        'cumulative_earned': round(running_cumulative, 2),
        'tx_count': len(txs),
        'categories_present': list(set(t['source'] for t in txs))
    })

peak_month_item = max(monthly_data, key=lambda x: x['earned'])

data['summary'] = {
    'total_earned': round(total_earned, 2),
    'total_transactions': len(data['transactions']),
    'agency_salary': round(sum(t['amount'] for t in data['transactions'] if t['category_id'] == 'agency'), 2),
    'college_freelance': round(sum(t['amount'] for t in data['transactions'] if t['category_id'] == 'college'), 2),
    'digital_products': round(sum(t['amount'] for t in data['transactions'] if t['category_id'] == 'digital'), 2),
    'razorpay': round(sum(t['amount'] for t in data['transactions'] if t['category_id'] == 'razorpay'), 2),
    'review_work': round(sum(t['amount'] for t in data['transactions'] if t['category_id'] == 'review'), 2),
    'peak_monthly_earning': round(peak_month_item['earned'], 2),
    'peak_month': peak_month_item['label']
}

data['monthly_timeline'] = monthly_data

with open('data.js', 'w', encoding='utf-8') as f:
    f.write('window.PORTFOLIO_DATA = ' + json.dumps(data, indent=2) + ';\n')

summary_export = {
    'currency': 'INR',
    'totals': data['summary'],
    'categories': data['categories'],
    'monthly_timeline': monthly_data
}
with open('master_financial_summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary_export, f, indent=2)

print(f"data.js and master_financial_summary.json regenerated successfully.")
print(f"Total Earned: INR {data['summary']['total_earned']:,.2f} across {data['summary']['total_transactions']} transactions.")
print(f"Peak Month: {data['summary']['peak_month']} at INR {data['summary']['peak_monthly_earning']:,.2f}.")
