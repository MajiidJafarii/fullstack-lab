import {
  useSyncExternalStore,
} from "react"


let authenticated = false


const listeners = new Set<
  () => void
>()


function subscribe(
  callback: () => void,
) {
  listeners.add(callback)

  return () => {
    listeners.delete(callback)
  }
}


function getSnapshot() {
  return authenticated
}


export function setAuthenticated(
  value: boolean,
) {
  authenticated = value

  listeners.forEach(
    (listener) => listener(),
  )
}


export function useSessionState() {
  return useSyncExternalStore(
    subscribe,
    getSnapshot,
  )
}
