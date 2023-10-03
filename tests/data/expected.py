from __future__ import annotations

EXPECTED_MD_DIFF = """
--- tests/data/test.md
+++ tests/data/test.md
@@ -2,11 +2,11 @@
 
 ## One
 
-abc https://github.com/python/python-docs-theme/pull/44 xyz
+abc [python/python-docs-theme#44](https://github.com/python/python-docs-theme/pull/44) xyz
 
-abc https://github.com/python/python-docs-theme/commit/bcb78b690e44a6f1662c75dde030a7852299fd14 xyz
+abc [python/python-docs-theme#bcb78b6](https://github.com/python/python-docs-theme/commit/bcb78b690e44a6f1662c75dde030a7852299fd14) xyz
 
-abc https://github.com/python/python-docs-theme/pull/44#issuecomment-1676720287 xyz
+abc [python/python-docs-theme#44 (comment)](https://github.com/python/python-docs-theme/pull/44#issuecomment-1676720287) xyz
 
 
 ## Two

"""  # noqa: E501, W293

EXPECTED_RST_DIFF = """
--- tests/data/test.rst
+++ tests/data/test.rst
@@ -5,11 +5,11 @@
 One
 ===
 
-abc https://github.com/python/python-docs-theme/pull/44 xyz
+abc `python/python-docs-theme#44 <https://github.com/python/python-docs-theme/pull/44>`__ xyz
 
-abc https://github.com/python/python-docs-theme/commit/bcb78b690e44a6f1662c75dde030a7852299fd14 xyz
+abc `python/python-docs-theme#bcb78b6 <https://github.com/python/python-docs-theme/commit/bcb78b690e44a6f1662c75dde030a7852299fd14>`__ xyz
 
-abc https://github.com/python/python-docs-theme/pull/44#issuecomment-1676720287 xyz
+abc `python/python-docs-theme#44 (comment) <https://github.com/python/python-docs-theme/pull/44#issuecomment-1676720287>`__ xyz
 
 Two
 ===

"""  # noqa: E501, W293

EXPECTED_TXT_DIFF = """
--- tests/data/test.txt
+++ tests/data/test.txt
@@ -2,11 +2,11 @@
 
 One
 
-abc https://github.com/python/python-docs-theme/pull/44 xyz
+abc python/python-docs-theme#44 xyz
 
-abc https://github.com/python/python-docs-theme/commit/bcb78b690e44a6f1662c75dde030a7852299fd14 xyz
+abc python/python-docs-theme#bcb78b6 xyz
 
-abc https://github.com/python/python-docs-theme/pull/44#issuecomment-1676720287 xyz
+abc python/python-docs-theme#44 (comment) xyz
 
 Two

"""  # noqa: E501, W293

EXPECTED_MD_NO_CHANGE = "no change for tests/data/test-no-change.md"
