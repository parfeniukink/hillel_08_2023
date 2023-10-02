from dataclasses import dataclass

CURRENCY_EXCHANGE_RATES: dict[str, dict[str, float]] = {
    "usd": {"usd": 1, "uah": 0.3, "gbp": 1.2},
    "uah": {"usd": 37.5, "uah": 1, "gbp": 38},
    "gbp": {"usd": 0.8, "uah": 0.2, "gbp": 1},
}


@dataclass
class Price:
    value: float
    currency: str

    __MIDDLE_CURRENCY = "usd"

    def convert(self, target: str) -> "Price":
        rate = CURRENCY_EXCHANGE_RATES[self.currency][target]
        return Price(value=self.value * rate, currency=target)

    def __add__(self, other: "Price") -> "Price":
        """
        We can perform math operatins between Price instances so you
        can ....

        Input data:
            the middle currency: usd

        The flow:
        1. If the left is not MI


        More examples:
            Double conversion
                self(!usd) + other(!usd)
                self(!usd) => self(usd)
                other(!usd) => other(usd)
                self(usd) + other(usd)
                return self(usd) => self(!usd)

            Left USD, other is NOT USD
                self(usd) + other(!usd)
                other(!usd) => other(usd)
                return self(usd) + other(usd)
        """

        if (
            self.currency.lower() != self.__MIDDLE_CURRENCY
            and other.currency.lower() != self.__MIDDLE_CURRENCY
        ):
            self_converted: "Price" = self.convert(self.__MIDDLE_CURRENCY)
            other_converted: "Price" = other.convert(self.__MIDDLE_CURRENCY)

            result_as_middle = Price(
                value=(self_converted.value + other_converted.value),
                currency=self.__MIDDLE_CURRENCY,
            )

            return result_as_middle.convert(target=self.currency)


left = Price(value=12, currency="uah")
right = Price(value=32, currency="gbp")

result: Price = left + right

print(result)
