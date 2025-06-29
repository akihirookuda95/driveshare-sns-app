from dataclasses import dataclass


@dataclass(frozen=True)
class Distance:
    """
    距離を表す値オブジェクト（キロメートル単位）
    """

    kilometers: float

    def __post_init__(self):
        """完全コンストラクタ - 不正な状態を防ぐための検証を行う"""
        if self.kilometers < 0:
            raise ValueError("距離はマイナス値にできません。")
        if self.kilometers > 10000: # 現実的な上限値
            raise ValueError("距離は10,000km以下である必要があります。")
