import { defineConfig } from "orval"

export default defineConfig({
  api: {
    input: {
      target:
        "http://127.0.0.1:8000/api/schema/?format=json",
    },

    output: {
      mode: "tags-split",

      target:
        "./src/shared/api/generated",

      schemas:
        "./src/shared/api/generated-types",

      client: "react-query",

      httpClient: "axios",

      clean: true,

      override: {
        mutator: {
          path:
            "./src/shared/api/http.ts",

          name: "apiClient",
        },
      },
    },
  },
})
