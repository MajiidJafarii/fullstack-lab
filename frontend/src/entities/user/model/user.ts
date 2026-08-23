export interface User {
  id: number

  email: string

  first_name: string

  last_name: string

  email_verified: boolean

  is_active: boolean

  is_staff: boolean

  is_superuser: boolean

  date_joined: string

  last_login: string | null
}
