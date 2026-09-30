"""Synthetic seasonal-naive baseline, separate from internal SARIMAX scripts.
Run: python forecast_demo.py
Uses the standard library. No corporate data or third-party dependencies.
"""
import csv
import math
from pathlib import Path
from statistics import mean

if __name__ == '__main__':
    series = [100 + 0.35 * i + 8 * math.sin(2 * math.pi * i / 12)
              for i in range(60)]
    train, test = series[:-12], series[-12:]
    prediction = train[-12:]
    mae = mean(abs(actual - pred) for actual, pred in zip(test, prediction))
    print(f'Synthetic holdout MAE: {mae:.2f} index points')
    output = Path('synthetic_baseline.csv')
    with output.open('w', newline='') as handle:
        writer = csv.writer(handle)
        writer.writerow(['holdout_month', 'synthetic_actual', 'seasonal_naive'])
        writer.writerows((i + 1, round(actual, 2), round(pred, 2))
                         for i, (actual, pred) in enumerate(zip(test, prediction)))
    print(f'Saved {output}. These results do not measure original model accuracy.')
