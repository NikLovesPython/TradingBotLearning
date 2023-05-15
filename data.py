import yfinance as yf
import pandas as pd

dataF = yf.download("EURUSD=X", start="2023-5-6",
                    end="2023-5-12", interval='15m')
