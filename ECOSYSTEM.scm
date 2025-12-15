;; SPDX-License-Identifier: AGPL-3.0-or-later
;; SPDX-FileCopyrightText: 2025 Jonathan D.A. Jewell
;; ECOSYSTEM.scm — my-newsroom

(ecosystem
  (version "1.0.0")
  (name "my-newsroom")
  (type "project")
  (purpose "**Version:** 0.1.0-alpha")

  (position-in-ecosystem
    "Part of hyperpolymath ecosystem. Follows RSR guidelines.")

  (related-projects
    (project (name "rhodium-standard-repositories")
             (url "https://github.com/hyperpolymath/rhodium-standard-repositories")
             (relationship "standard")))

  (what-this-is "**Version:** 0.1.0-alpha")
  (what-this-is-not "- NOT exempt from RSR compliance"))
