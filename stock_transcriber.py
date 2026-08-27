import urllib.request
import re
import csv
import datetime

def fetch_zeebiz_url(url):
    """Fetch HTML content from zeebiz URL using standard library"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return response.read().decode('utf-8', errors='replace')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_zeebiz_article(html, date_str):
    """Parse zeebiz market strategy article for stock recommendations"""
    text = html
    
    record = {
        'date': date_str,
        'nifty_support': [],
        'nifty_resistance': [],
        'nifty_bank_support': [],
        'nifty_bank_resistance': [],
        'nifty_intraday_sl': [],
        'nifty_bank_intraday_sl': [],
        'targets': [],
        'buy_ranges': [],
        'sell_ranges': [],
        'stock_picks': []
    }
    
    # Extract Nifty support levels
    for m in re.finditer(r'Nifty.*?support.*?at\s+([\d,\s-]+)', text, re.IGNORECASE):
        record['nifty_support'].append(m.group(1).strip())
    
    # Extract Nifty resistance levels
    for m in re.finditer(r'Nifty.*?resistance.*?at\s+([\d,\s-]+)', text, re.IGNORECASE):
        record['nifty_resistance'].append(m.group(1).strip())
    
    # Extract Nifty Bank support
    for m in re.finditer(r'Nifty Bank.*?support.*?at\s+([\d,\s-]+)', text, re.IGNORECASE):
        record['nifty_bank_support'].append(m.group(1).strip())
    
    # Extract Nifty Bank resistance
    for m in re.finditer(r'Nifty Bank.*?resistance.*?at\s+([\d,\s-]+)', text, re.IGNORECASE):
        record['nifty_bank_resistance'].append(m.group(1).strip())
    
    # Extract Nifty stop loss
    for m in re.finditer(r'Nifty.*?stop loss at\s+([\d,]+)', text, re.IGNORECASE):
        record['nifty_intraday_sl'].append(m.group(1).strip())
    
    # Extract Nifty Bank stop loss
    for m in re.finditer(r'Nifty Bank.*?stop loss at\s+([\d,]+)', text, re.IGNORECASE):
        record['nifty_bank_intraday_sl'].append(m.group(1).strip())
    
    # Extract target prices
    for m in re.finditer(r'target.*?of\s+Rs?\s*([\d,]+)', text, re.IGNORECASE):
        record['targets'].append(m.group(1).strip())
    
    # Extract buy ranges
    for m in re.finditer(r'buy.*?in the\s+([\d,-]+)\s+range', text, re.IGNORECASE):
        record['buy_ranges'].append(m.group(1).strip())
    
    # Extract sell ranges
    for m in re.finditer(r'sell.*?in the\s+([\d,-]+)\s+range', text, re.IGNORECASE):
        record['sell_ranges'].append(m.group(1).strip())
    
    # Extract specific stock recommendations: "- StockName - Target Rs X with stop loss at Rs Y"
    # Pattern found in zeebiz strategy articles
    stock_pattern = re.findall(
        r'-\s+([A-Za-z&\s]+?)\s+-\s+Target\s+Rs?\s*([\d,]+)\s+with\s+stop loss\s+at\s+Rs?\s*([\d,]+)',
        text
    )
    for stock_name, target, sl in stock_pattern:
        record['stock_picks'].append({
            'name': stock_name.strip(),
            'target': target,
            'stop_loss': sl
        })
    
    # Deduplicate while preserving order
    for key in record:
        if isinstance(record[key], list) and key != 'stock_picks':
            record[key] = list(dict.fromkeys(record[key]))
    
    return record

def write_csv(record, filename=None):
    """Write parsed data to CSV file"""
    if filename is None:
        filename = f"zeebiz_stocks_{record['date']}.csv"
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Write title
        writer.writerow([f"Zee Business Stock Recommendations - {record['date']}"])
        writer.writerow([])
        
        # Write headers
        writer.writerow(['Category', 'Level/Range', 'Details'])
        
        # Nifty support
        if record['nifty_support']:
            writer.writerow(['Nifty50 Support', ', '.join(record['nifty_support']), 'Intraday support levels'])
        
        # Nifty resistance
        if record['nifty_resistance']:
            writer.writerow(['Nifty50 Resistance', ', '.join(record['nifty_resistance']), 'Resistance levels'])
        
        # Nifty Bank support
        if record['nifty_bank_support']:
            writer.writerow(['Nifty Bank Support', ', '.join(record['nifty_bank_support']), 'Intraday support levels'])
        
        # Nifty Bank resistance
        if record['nifty_bank_resistance']:
            writer.writerow(['Nifty Bank Resistance', ', '.join(record['nifty_bank_resistance']), 'Resistance levels'])
        
        # Nifty intraday SL
        if record['nifty_intraday_sl']:
            writer.writerow(['Nifty50 Intraday SL', ', '.join(record['nifty_intraday_sl']), 'Intraday stop loss'])
        
        # Nifty Bank intraday SL
        if record['nifty_bank_intraday_sl']:
            writer.writerow(['Nifty Bank Intraday SL', ', '.join(record['nifty_bank_intraday_sl']), 'Intraday stop loss'])
        
        # Targets
        if record['targets']:
            writer.writerow(['Target Prices', ', '.join(record['targets'][:5]), 'Profit targets'])
        
        # Buy ranges
        if record['buy_ranges']:
            writer.writerow(['Buy Ranges', ', '.join(record['buy_ranges']), 'Aggressive buy range'])
        
        # Sell ranges
        if record['sell_ranges']:
            writer.writerow(['Sell Ranges', ', '.join(record['sell_ranges']), 'Aggressive sell range'])
        
        # Stock picks
        if record['stock_picks']:
            writer.writerow([])  # Empty row
            writer.writerow(['Specific Stock Picks', 'Target', 'Stop Loss'])
            for sp in record['stock_picks'][:8]:
                writer.writerow([sp['name'], sp['target'], sp['stop_loss']])
    
    print(f"CSV file saved as: {filename}")
    return filename

def main():
    # Get today's date
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # Zeebiz market strategy articles with entry/exit/SL data
    # Based on search results, these article types contain the data our dad needs
    test_urls = [
        "https://www.zeebiz.com/market-news/news-nifty50-strong-sell-zone-at-23900-24000-says-anil-singhvi-key-levels-to-track-395566",
        "https://www.zeebiz.com/market-news/news-share-market-strategy-nifty50-strong-support-at-21700-22000-as-middle-east-tensions-ease-anil-singhvi-weighs-in-392489",
        "https://www.zeebiz.com/market-news/news-anil-singhvi-market-strategy-december-29-how-to-trade-nifty-50-nifty-bank-today-386656",
    ]
    
    all_records = []
    
    for url in test_urls:
        print(f"Trying: {url}")
        html = fetch_zeebiz_url(url)
        if html:
            record = parse_zeebiz_article(html, date_str)
            all_records.append(record)
            print(f"  Parsed {len(record['nifty_support'])} Nifty support, "
                  f"{len(record['nifty_bank_intraday_sl'])} Bank SL, "
                  f"{len(record['stock_picks'])} stock picks")
        else:
            print(f"  Skipped (could not fetch)")
    
    if not all_records:
        print("No articles fetched. Creating empty template.")
        all_records = [{"date": date_str, 
                        'nifty_support': [], 
                        'nifty_resistance': [], 
                        'nifty_bank_support': [], 
                        'nifty_bank_resistance': [], 
                        'nifty_intraday_sl': [], 
                        'nifty_bank_intraday_sl': [], 
                        'targets': [], 
                        'buy_ranges': [], 
                        'sell_ranges': [], 
                        'stock_picks': []}]
    
    record = all_records[0]
    
    # Write to CSV
    filename = write_csv(record)
    
    # Print summary
    print(f"\n=== Summary for {date_str} ===")
    print(f"Nifty Support: {', '.join(record['nifty_support']) if record['nifty_support'] else 'None found'}")
    print(f"Nifty Resistance: {', '.join(record['nifty_resistance']) if record['nifty_resistance'] else 'None found'}")
    print(f"Nifty Bank Support: {', '.join(record['nifty_bank_support']) if record['nifty_bank_support'] else 'None found'}")
    print(f"Nifty Bank Resistance: {', '.join(record['nifty_bank_resistance']) if record['nifty_bank_resistance'] else 'None found'}")
    print(f"Nifty Intraday SL: {', '.join(record['nifty_intraday_sl']) if record['nifty_intraday_sl'] else 'None found'}")
    print(f"Nifty Bank Intraday SL: {', '.join(record['nifty_bank_intraday_sl']) if record['nifty_bank_intraday_sl'] else 'None found'}")
    print(f"Targets: {', '.join(record['targets'][:5]) if record['targets'] else 'None found'}")
    print(f"Buy Ranges: {', '.join(record['buy_ranges']) if record['buy_ranges'] else 'None found'}")
    print(f"Sell Ranges: {', '.join(record['sell_ranges']) if record['sell_ranges'] else 'None found'}")
    print(f"Stock Picks: {len(record['stock_picks'])} found")
    print(f"\nCSV file: {filename}")
    print(f"Open this file in Excel for your dad's daily trading reference (9:15 AM - 3:30 PM)")

if __name__ == "__main__":
    main()