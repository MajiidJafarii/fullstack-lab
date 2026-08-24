import type {
  BlogPostsListQueryResult,
} from "@/shared/api"


export type Post =
  BlogPostsListQueryResult["results"][number]
