import axios from '@/libs/api.request'

export const login = ({ name, password }) => {
  const data = {
    name,
    password
  }
  return axios.request({
    url: 'auth/login',
    data,
    method: 'post'
  })
}

export const getUserInfo = (token) => {
  return axios.request({
    url: 'auth/me',
    params: {
      token
    },
    method: 'post'
  })
}
/**
    人员列表
    输入：token
    返回：所有人员
*/
export const getUserList = (token) => {
  return axios.request({
    url: 'v1/users/',
    params: {
      token
    },  
    method: 'get'
  })
}
/**
    人员新增
    输入：token, 
    返回：
*/
export const getUseradd = (token,info) => {
  return axios.request({
    url: 'v1/users/add',
    params: {
      token
    },
    data: info,
    method: 'post'
  })
}
/**
    人员信息
    输入：token, 
    返回：
*/
export const getUserView = (token,user_code) => {
  return axios.request({
    url: 'v1/users/'+user_code,
    params: {
      token,
      user_code     
    }, 
    method: 'get'
  })
}
/**
    人员信息token
    输入：token, 
    返回：
*/
export const getUser = (token) => {
  return axios.request({
    url: 'v1/users/1',
    params: {
      token
    },  
    method: 'get'
  })
}
export const logout = (token) => {
  return axios.request({
    url: 'auth/logout',
    params: {
      token
    },  
    method: 'post'
  })
}

