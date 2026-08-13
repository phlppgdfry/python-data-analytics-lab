"""Automatische controles voor de sales-cleaninglogica."""

import pandas as pd
import pytest

from src.cleaning import clean_sales_data


def test_clean_sales_data_removes_invalid_and_duplicate_rows():
    raw_sales = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4, 5, 1],
            "country": [
                "Belgium",
                "belgium",
                "Belgium ",
                "France",
                "Netherlands",
                "Belgium",
            ],
            "product": ["Shoes", "Shirt", "Jacket", "Shoes", "Jacket", "Shoes"],
            "quantity": [2, 1, 1, 1, "two", 2],
            "price": [89.99, "49,99", 129.99, None, 129.99, 89.99],
        }
    )

    cleaned_sales = clean_sales_data(raw_sales)

    assert len(cleaned_sales) == 3
    assert cleaned_sales["country"].unique().tolist() == ["Belgium"]
    assert cleaned_sales["revenue"].sum() == pytest.approx(359.96)
