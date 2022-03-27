"""
How To Get Financial Data from Yahoo Finance with Python
https://youtu.be/39zpZ0tK-XI
YouTube Channel: Asim Code
"""
import yfinance as yf

goog = yf.Ticker("GOOGL")
print(goog.info)

hist = goog.history(period="max")
print(hist)
print(goog.dividends)
print(goog.splits)
