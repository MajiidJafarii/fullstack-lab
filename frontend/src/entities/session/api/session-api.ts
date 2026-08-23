import {
  useAuthLoginCreate,
  useAuthLogoutCreate,
  useAuthRefreshCreate,
} from "@/shared/api"

export function useLogin() {
  return useAuthLoginCreate()
}


export function useLogout() {
  return useAuthLogoutCreate()
}


export function useRefreshToken() {
  return useAuthRefreshCreate()
}
