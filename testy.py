import unittest

from KMP_sample import kmp_tablica


class TestKMPAlgorithm(unittest.TestCase):

    def test_general_case(self):
        text = "abcxyzdefabc"
        pattern = "abc"
        self.assertGreaterEqual(kmp_search(text, pattern), 1)

    def test_no_match(self):
        text = "abcdefgh"
        pattern = "xyz"
        self.assertEqual(kmp_search(text, pattern), 0)

    def test_pattern_at_beginning(self):
        text = "abcxyz"
        pattern = "abc"
        self.assertGreaterEqual(kmp_search(text, pattern), 1)

    def test_pattern_at_end(self):
        text = "xyzabc"
        pattern = "abc"
        self.assertGreaterEqual(kmp_search(text, pattern), 1)

    def test_multiple_pattern_occurrences(self):
        text = "ababab"
        pattern = "ab"
        self.assertGreaterEqual(kmp_search(text, pattern), 3)

    def test_empty_pattern(self):
        text = "abcdefgh"
        pattern = ""
        self.assertEqual(kmp_search(text, pattern), len(text) + 1)  # Oczekujemy jednego więcej dopasowania niż długość tekstu


    def test_empty_text(self):
        text = ""
        pattern = "abc"
        self.assertEqual(kmp_search(text, pattern), 0)

    def test_text_only_pattern_repeats(self):
        text = "abcabcabc"
        pattern = "abc"
        self.assertEqual(kmp_search(text, pattern), len(text)//len(pattern))

    # def test_long_text_and_pattern(self):
    #     text = "a" * 10**4 + "b" * 10**4 + "c" * 10**4
    #     pattern = "b" * 10**4
    #     self.assertGreaterEqual(kmp_search(text, pattern), 1)

    def test_unique_characters_in_text(self):
        text = "abcdefgh"
        pattern = "xyz"
        self.assertEqual(kmp_search(text, pattern), 0)


# Poniżej dodatkowe funkcje potrzebne do przeprowadzenia testów
def kmp_search(text, pattern):
    tablica_dopasowan = kmp_tablica(pattern)
    indeks_tekstu = 0
    indeks_wzorca = 0
    ilosc_wzorcow = 0

    while indeks_tekstu < len(text):
        if pattern[indeks_wzorca] == text[indeks_tekstu]:
            indeks_tekstu += 1
            indeks_wzorca += 1

            if indeks_wzorca == len(pattern):
                ilosc_wzorcow += 1
                indeks_wzorca = tablica_dopasowan[indeks_wzorca]

        else:
            if indeks_wzorca != 0:
                indeks_wzorca = tablica_dopasowan[indeks_wzorca]
            else:
                indeks_tekstu += 1

    return ilosc_wzorcow


# Pozostała część kodu - wczytywanie z pliku, przykład użycia, itp.

if __name__ == "__main__":
    unittest.main()
