import {
  useAuth,
} from "@/entities/session"


import {
  useAuthLoginCreate,
} from "@/shared/api"



export function useLoginAction() {


  const {
    loginSuccess,
  } = useAuth()



  const mutation =
    useAuthLoginCreate()



  async function login(
    email: string,
    password: string,
  ) {


    const response =
      await mutation.mutateAsync({

        data: {
          email,
          password,
        },

      })


    loginSuccess()


    return response

  }



  return {

    login,

    isPending:
      mutation.isPending,

    error:
      mutation.error,

  }

}
