import {
  useMeRetrieve,
} from "@/shared/api"


export function useCurrentUser(
  enabled = true,
) {
  return useMeRetrieve({
    query: {
      enabled,
    },
  })
}
