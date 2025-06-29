from dataclasses import dataclass


@dataclass(frozen=True)
class DifficultyLevel:
    """
    難易度を表す値オブジェクト(1-3の整数値)
    """

    value: int

    def __post_init__(self):
        """
        完全コンストラクタ - 不正な状態を防ぐための検証を行う
        """
        if not isinstance(self.value, int):
            raise ValueError("難易度は整数である必要があります。")
        if not 1 <= self.value <= 3:
            raise ValueError("難易度は1-3の範囲である必要があります。")