import axios from "axios"

import type {
  AxiosRequestConfig,
} from "axios"



function getCookie(
  name: string,
) {

  const value =
    `; ${document.cookie}`

  const parts =
    value.split(`; ${name}=`)


  if (parts.length === 2) {

    return parts
      .pop()
      ?.split(";")
      .shift()

  }

}



const instance =
  axios.create({

    baseURL:
      import.meta.env.VITE_API_URL,

    withCredentials: true,

  })



instance.interceptors.request.use(
  (config) => {

    const csrf =
      getCookie("csrftoken")


    if (csrf) {

      config.headers["X-CSRFToken"] =
        csrf

    }


    return config

  }
)



export const apiClient = async <T>(
  config: AxiosRequestConfig,
  options?: AxiosRequestConfig,
): Promise<T> => {


  const response =
    await instance.request<T>({
      ...config,
      ...options,
    })


  return response.data

}



export const api = instance
