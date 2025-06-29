from dataclasses import dataclass


@dataclass(frozen=True)
class Duration:
    """
    所要時間を表す値オブジェクト（分単位）
    """

    minutes: int

    def __post_init__(self):
        """完全コンストラクタ - 不正な状態を防ぐための検証を行う"""
        if self.minutes < 0:
            raise ValueError("所要時間はマイナス値にできません。")
        if self.minutes > 1440: # 24時間 = 1440分
            raise ValueError("所要時間は24時間（1440分）以下である必要があります。")