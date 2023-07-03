# Release Checklist

- [ ] Get `main` to the appropriate code release state.
      [GitHub Actions](https://github.com/hugovk/linkotron/actions) should be running
      cleanly for all merges to `main`.
      [![GitHub Actions status](https://github.com/hugovk/linkotron/workflows/Test/badge.svg)](https://github.com/hugovk/linkotron/actions)

- [ ] Edit release draft, adjust text if needed:
      https://github.com/hugovk/linkotron/releases

- [ ] Check next tag is correct, amend if needed

- [ ] Publish release

- [ ] Check the tagged
      [GitHub Actions build](https://github.com/hugovk/linkotron/actions/workflows/deploy.yml)
      has deployed to [PyPI](https://pypi.org/project/linkotron/#history)

- [ ] Check installation:

```bash
pip3 uninstall -y linkotron && pip3 install -U linkotron && linky --version
```
