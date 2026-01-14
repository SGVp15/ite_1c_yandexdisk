from unittest import TestCase

from rename_exam_excel import replace_string


class Test(TestCase):
    def test_replace_string(self):
        assert replace_string('"1 Что нами."') == '"1 Что нами."'
        assert replace_string('"1 Что нами?"') == '"1 Что нами?"'
        assert replace_string('1 Что нами.') == '1 Что нами.'
        assert replace_string('1 Что нами') == '1 Что нами.'
        assert replace_string('1 Что нами:') == '1 Что нами:'
        assert replace_string('1 Что нами?') == '1 Что нами?'
        assert replace_string('1 Что нами:') == '1 Что нами:'
        assert replace_string('1 Что нами; ') == '1 Что нами;'
        assert replace_string('1 Что нами ,  ') == '1 Что нами,'
        assert replace_string('"') == '"'
        assert replace_string('''Что НЕ входит в типовой набор требований к соискателю?
        ''') == 'Что НЕ входит в типовой набор требований к соискателю?'
