// store.ts
import { InjectionKey } from 'vue'
import { createStore, useStore as baseStore, Store } from 'vuex'

// 为 store state 声明类型
export interface State {
    count: number
    collapse: boolean
}

// 定义 injection key
export const key: InjectionKey<Store<State>> = Symbol()

export const store = createStore<State>({
    state: {
        count: 0,
        collapse: false
    },
    mutations: {
        setCount(state: State, count: number) {
            state.count = count;
        },
        setCollapse: (state: State, collapse: boolean) => {
            state.collapse = collapse
        }
    },
    getters: {
        getCount(state: State) {
            return state.count
        },
        getCollapse:(state: State)=>{
            return state.collapse
        }
    }
})

export function useStore() {
    return baseStore(key)
}