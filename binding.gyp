{
  "targets": [
    {
      "target_name": "tree_sitter_python_legesher_binding",
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "src"
      ],
      "sources": [
        "src/parser.c",
        "src/binding.cc",
        "src/scanner.cc"
      ],
      "cflags_c": [
        "-std=c99",
      ]
    }
  ]
}
