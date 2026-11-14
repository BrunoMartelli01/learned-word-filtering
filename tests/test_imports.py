"""Every module of the package imports (needs the analysis environment of requirements.txt, no data)."""
import importlib
import pkgutil
import unittest

# scripts that read sys.argv or create the run view directory when they are imported
SCRIPT_STYLE = {'wordfilter.figures.make_fig56', 'wordfilter.second_stage.read_native', 'wordfilter.reruns.exact.report'}


class ImportAll(unittest.TestCase):
    def test_every_module_imports(self):
        import wordfilter
        failed = []
        for m in pkgutil.walk_packages(wordfilter.__path__, 'wordfilter.'):
            if m.name in SCRIPT_STYLE:
                continue
            try:
                importlib.import_module(m.name)
            except Exception as e:   # collect every failure, then report them together
                failed.append((m.name, repr(e)))
        self.assertEqual(failed, [])


if __name__ == '__main__':
    unittest.main()
