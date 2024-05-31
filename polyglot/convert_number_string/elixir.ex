defmodule ConvertNumberString do
  @spec to_english(integer) :: String.t
  def to_english(number) do
    case number do
      0 -> "Zero"
      _ -> to_english(number, 0)
    end
  end

  @spec to_english(integer, integer) :: String.t
  defp to_english(number, _power) do
    case number do
      0 -> ""
      1 -> "One"
      2 -> "Two"
      3 -> "Three"
      4 -> "Four"
      5 -> "Five"
      6 -> "Six"
      7 -> "Seven"
      8 -> "Eight"
      9 -> "Nine"
      10 -> "Ten"
      11 -> "Eleven"
      12 -> "Twelve"
      13 -> "Thirteen"
      14 -> "Fourteen"
      15 -> "Fifteen"
      16 -> "Sixteen"
      17 -> "Seventeen"
      18 -> "Eighteen"
      19 -> "Nineteen"
      20 -> "Twenty"
      30 -> "Thirty"
      40 -> "Forty"
      50 -> "Fifty"
      60 -> "Sixty"
      70 -> "Seventy"
      80 -> "Eighty"
      90 -> "Ninety"
      _ when number < 100 -> to_english(number - rem(number, 10)) <> " " <> to_english(rem(number, 10), 0)
      _ when number < 1000 -> to_english(div(number, 100), 2) <> " Hundred " <> to_english(rem(number, 100), 0)
      _ when number < 1000000 -> to_english(div(number, 1000), 3) <> " Thousand " <> to_english(rem(number, 1000), 0)
      _ when number < 1000000000 -> to_english(div(number, 1000000), 6) <> " Million " <> to_english(rem(number, 1000000), 0)
      _ when number < 1000000000000 -> to_english(div(number, 1000000000), 9) <> " Billion " <> to_english(rem(number, 1000000000), 0)
      _ -> "Number is too large"
    end
  end

  def result(number) do
    number
    |> to_english()
    |> String.trim()
  end
end

dbg(ConvertNumberString.result(0))
dbg(ConvertNumberString.result(1000))
dbg(ConvertNumberString.result(234))
dbg(ConvertNumberString.result(312))
dbg(ConvertNumberString.result(999999999999))
